#!/usr/bin/env python3

# Present skeleton file for 50.042 FCS


# constants
from asyncio.format_helpers import extract_stack


FULLROUND = 31

# S-Box Layer
sbox = [0xC, 0x5, 0x6, 0xB, 0x9, 0x0, 0xA, 0xD,
        0x3, 0xE, 0xF, 0x8, 0x4, 0x7, 0x1, 0x2]

# PLayer
pmt = [0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51,
        4, 20, 36, 52, 5, 21, 37, 53, 6, 22, 38, 54, 7, 23, 39, 55,
        8, 24, 40, 56, 9, 25, 41, 57, 10, 26, 42, 58, 11, 27, 43, 59,
        12, 28, 44, 60, 13, 29, 45, 61, 14, 30, 46, 62, 15, 31, 47, 63]

# Rotate left: 0b1001 --> 0b0011


def rol(val, r_bits, max_bits): return \
    (val << r_bits % max_bits) & (2**max_bits - 1) | \
    ((val & (2**max_bits - 1)) >> (max_bits - (r_bits % max_bits)))

# Rotate right: 0b1001 --> 0b1100


def ror(val, r_bits, max_bits): return \
    ((val & (2**max_bits - 1)) >> r_bits % max_bits) | \
    (val << (max_bits - (r_bits % max_bits)) & (2**max_bits - 1))


def genRoundKeys(key):
    #mask then shift then OR
    #First part of algorithm - [k79k78...k0] = [k18k17...k20k19]
    result = {}
    result[0] = 32
    
    msb_initial_mask = 0xffffffffffffffff0000
    result_1 = key & msb_initial_mask
    result_1 = result_1 >> 16
    result[1] = result_1
    
    temp_dict = {}
    temp_dict[0] = 32
    temp_dict[1] = key
    
    for round_counter in range(1, 33):
        #need the left most 61 bits
        lm61_mask = 0xfffffffffffffff80000
        rm19_mask = 0x0000000000000007ffff

        lm61 = temp_dict[round_counter] & lm61_mask
        lm61 = lm61 >> 19

        rm19 = temp_dict[round_counter] & rm19_mask
        rm19 = rm19 << 61

        first = rm19 | lm61
        #Second part of algorithm - [k79k78k77k76] = S[k79k78k77k76]
        msc_mask = 0xf0000000000000000000
        msc = first & msc_mask
        msc = msc >> 76 #76 because one hex character is 4 bits
        new_msc = sbox[msc]
        new_msc = new_msc << 76

        temp = first & ~msc_mask
        second = new_msc | temp

        #Third part of algorithm - [k19k18k17k16k15] ⊕ round_counter
        third_mask = 0xf8000
        extract_19_15 = second & third_mask
        
        five_bits = extract_19_15 >> 15
        new_five_bits = five_bits ^ round_counter 
        new_five_bits_pos = new_five_bits << 15
        replace_original_0 = second & ~third_mask
        third = replace_original_0 | new_five_bits_pos
        
        temp_dict[round_counter+1] = third
        
        msb64_mask = 0xffffffffffffffff0000
        final = third & msb64_mask
        final = final >> 16
        result[round_counter+1] = final
    return result

def addRoundKey(state, Ki):
    return state ^ Ki


def sBoxLayer(state):
    result = state
    for x in range(15, -1, -1):
        mask = 0xf << (4*x)
        extract = result & mask
        isolate = extract >> (4*x)
        replacement = sbox[isolate]

        replacement_pos = replacement << (4*x)
        not_extract = result & ~mask
        result = not_extract | replacement_pos
    return result
    

def sBoxLayer_inv(state):
    result = state
    for x in range(15, -1, -1):
        mask = 0xf << (4*x)
        extract = result & mask
        isolate = extract >> (4*x)
        
        replacement = sbox.index(isolate)

        replacement_pos = replacement << (4*x)
        not_extract = result & ~mask
        result = not_extract | replacement_pos
    return result

def pLayer(state):
    result = state 
    original_ls = []
    ret = 0x0
    for x in range(0, 64):
        mask = 0x1 << x
        extract = result & mask
        isolate = extract >> x
        original_ls.append(isolate)
    for new in range(0,64):
        position = pmt[new]
        current = original_ls[new]
        replacement_pos = current << position
        ret = ret | replacement_pos
    return ret
    

def pLayer_inv(state):
    result = state  
    original_ls = []
    ret = 0x0
    for x in range(0, 64):
        mask = 0x1 << x
        extract = result & mask
        isolate = extract >> x
        original_ls.append(isolate)
    for new in range(0,64):
        position = pmt[new]
        current = original_ls[position]
        replacement_pos = current << new
        ret = ret | replacement_pos
    return ret

def present_round(state, roundKey):
    result = addRoundKey(state, roundKey)
    result = sBoxLayer(result)
    result = pLayer(result)
    return result


def present_inv_round(state, roundKey):
    result = pLayer_inv(state)
    result = sBoxLayer_inv(result)
    result = addRoundKey(result, roundKey)
    return result


def present(plain, key):
    K = genRoundKeys(key)
    state = plain
    for i in range(1, FULLROUND + 1):
        state = present_round(state, K[i])
    state = addRoundKey(state, K[32])
    return state


def present_inv(cipher, key):
    K = genRoundKeys(key)
    state = cipher
    state = addRoundKey(state, K[32])
    for i in range(FULLROUND, 0, -1):
        state = present_inv_round(state, K[i])
    return state

if __name__ == "__main__":
    # Testvector for key schedule
    key1 = 0x00000000000000000000
    keys = genRoundKeys(key1)
    keysTest = {0: 32, 1: 0, 2: 13835058055282163712, 3: 5764633911313301505, 4: 6917540022807691265, 5: 12682149744835821666, 6: 10376317730742599722, 7: 442003720503347, 8: 11529390968771969115, 9: 14988212656689645132, 10: 3459180129660437124, 11: 16147979721148203861, 12: 17296668118696855021, 13: 9227134571072480414, 14: 4618353464114686070, 15: 8183717834812044671, 16: 1198465691292819143, 17: 2366045755749583272, 18: 13941741584329639728, 19: 14494474964360714113, 20: 7646225019617799193, 21: 13645358504996018922, 22: 554074333738726254, 23: 4786096007684651070, 24: 4741631033305121237, 25: 17717416268623621775, 26: 3100551030501750445, 27: 9708113044954383277, 28: 10149619148849421687, 29: 2165863751534438555, 30: 15021127369453955789, 31: 10061738721142127305, 32: 7902464346767349504}
    for k in keysTest.keys():
        assert keysTest[k] == keys[k]

    # Testvectors for single rounds without keyscheduling
    plain1 = 0x0000000000000000
    key1 = 0x00000000000000000000
    round1 = present_round(plain1, key1)
    round11 = 0xffffffff00000000
    assert round1 == round11

    round2 = present_round(round1, key1)
    round22 = 0xff00ffff000000
    assert round2 == round22

    round3 = present_round(round2, key1)
    round33 = 0xcc3fcc3f33c00000
    assert round3 == round33

    # invert single rounds
    plain11 = present_inv_round(round1, key1)
    assert plain1 == plain11
    plain22 = present_inv_round(round2, key1)
    assert round1 == plain22
    plain33 = present_inv_round(round3, key1)
    assert round2 == plain33
    
    # Everything together
    plain1 = 0x0000000000000000
    key1 = 0x00000000000000000000
    cipher1 = present(plain1, key1)
    plain11 = present_inv(cipher1, key1)
    assert plain1 == plain11

    plain2 = 0x0000000000000000
    key2 = 0xFFFFFFFFFFFFFFFFFFFF
    cipher2 = present(plain2, key2)
    plain22 = present_inv(cipher2, key2)
    assert plain2 == plain22

    plain3 = 0xFFFFFFFFFFFFFFFF
    key3 = 0x00000000000000000000
    cipher3 = present(plain3, key3)
    plain33 = present_inv(cipher3, key3)
    assert plain3 == plain33

    plain4 = 0xFFFFFFFFFFFFFFFF
    key4 = 0xFFFFFFFFFFFFFFFFFFFF
    cipher4 = present(plain4, key4)
    plain44 = present_inv(cipher4, key4)
    assert plain4 == plain44
