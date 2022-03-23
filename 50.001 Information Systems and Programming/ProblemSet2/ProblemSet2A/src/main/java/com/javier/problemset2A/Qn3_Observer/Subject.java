package com.javier.problemset2A.Qn3_Observer;

interface Subject {
    void register(Observer o);

    void unregister(Observer o);

    void notifyObservers();
}
