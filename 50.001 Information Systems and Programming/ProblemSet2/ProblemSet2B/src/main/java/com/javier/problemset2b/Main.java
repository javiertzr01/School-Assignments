package com.javier.problemset2b;

import javax.sound.midi.MidiUnavailableException;

import midi.Midi;
import music.Pitch;
import piano.PianoMachine;

public class Main {
    public static void main(String[] args) throws MidiUnavailableException, InterruptedException {
//        try {
//            Midi midi;
//            PianoMachine pm;
//            midi = Midi.getInstance();
//            midi.clearHistory();
//            pm = new PianoMachine();

            //First Test Case
//            pm.beginNote(new Pitch(0));
//            pm.beginNote(new Pitch(0));
//            Midi.rest(50);
//            pm.endNote(new Pitch(0));
//            System.out.println(midi.history());
//            midi.clearHistory();

            //Second Test Case
//            pm.beginNote(new Pitch(0));
//            Midi.rest(50);
//            pm.endNote(new Pitch(2));
//            System.out.println(midi.history());
//            midi.clearHistory();


            //Third Test Case
//            pm.beginNote(new Pitch(0));
//            pm.beginNote(new Pitch(2));
//            Midi.rest(100);
//            pm.endNote(new Pitch(0));
//            pm.endNote(new Pitch(2));
//            System.out.println(midi.history());
//            midi.clearHistory();

//        } catch (MidiUnavailableException e) {
//            e.printStackTrace();
//        }


            new TestQ1Hw().test();
    }
}