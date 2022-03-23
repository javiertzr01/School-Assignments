package piano;

import java.util.ArrayList;
import java.util.HashMap;

import javax.sound.midi.MidiUnavailableException;

import midi.Instrument;
import midi.Midi;
import music.NoteEvent;
import music.Pitch;

public class PianoMachine {
	
	private Midi midi;
	private HashMap<Pitch, Boolean> state;
	private Instrument instrument;
	private int adjustments;
	private ArrayList<NoteEvent> sequence;
	private boolean recording;
    
	/**
	 * constructor for PianoMachine.
	 * 
	 * initialize midi device and any other state that we're storing.
	 */
    public PianoMachine() {
    	try {
            midi = Midi.getInstance();
            state = new HashMap<Pitch, Boolean>();
            instrument = Midi.DEFAULT_INSTRUMENT;
            adjustments = 0;
            sequence = new ArrayList<NoteEvent>();
            recording = false;
        } catch (MidiUnavailableException e1) {
            System.err.println("Could not initialize midi device");
            e1.printStackTrace();
            return;
        }
    }

    public void beginNote(Pitch rawPitch) {

        Pitch adjustedPitch = rawPitch.transpose(adjustments);
        NoteEvent beginNoteEvent = new NoteEvent(adjustedPitch, System.currentTimeMillis(), instrument, NoteEvent.Kind.start);

        if (state.containsKey(adjustedPitch)) {
            if (state.get(adjustedPitch)){
                return;
            }
            else{
                midi.beginNote(adjustedPitch.toMidiFrequency(), instrument);
                state.put(adjustedPitch, true);
                if (recording){
                    sequence.add(beginNoteEvent);
                }
            }
        }
        else{
            midi.beginNote(adjustedPitch.toMidiFrequency(), instrument);
            state.put(adjustedPitch, true);
            if (recording){
                sequence.add(beginNoteEvent);
            }
        }
    }

    public void endNote(Pitch rawPitch) {

        Pitch adjustedPitch = rawPitch.transpose(adjustments);
        NoteEvent endNoteEvent = new NoteEvent(adjustedPitch, System.currentTimeMillis(), instrument, NoteEvent.Kind.stop);

        if (state.containsKey(adjustedPitch)) {
            if (state.get(adjustedPitch)) {
                midi.endNote(adjustedPitch.toMidiFrequency(), instrument);
                state.put(adjustedPitch, false);
                if (recording){
                    sequence.add(endNoteEvent);
                }
            }
            else {
                return;
            }
        }
    }

    public void changeInstrument() {
        instrument = instrument.next();
    }

    public void shiftUp() {
        if (adjustments < 24){
            adjustments += 12;
        }
    }

    public void shiftDown() {
        if (adjustments > -24){
            adjustments -= 12;
        }
    }

    public boolean toggleRecording() {
        if(recording){
            recording = false;
        }
        else {
            recording = true;
        }
    	return false;
    }

    public void playback() {
        long now = -1;
        for(NoteEvent n: sequence){
            if (now == -1){
                now = n.getTime();
            }
            else if (n.getTime() != now) {
                long end = n.getTime();
                long duration = (end - now)/10;
                Midi.rest((int) duration);
                now = n.getTime();
            }
            if(n.getKind() == NoteEvent.Kind.start){
                midi.beginNote(n.getPitch().toMidiFrequency(), n.getInstr());
                }
            else {
                midi.endNote(n.getPitch().toMidiFrequency(), n.getInstr());
            }
        }
        //clear sequence ArrayList
        sequence.clear();
    }

}
