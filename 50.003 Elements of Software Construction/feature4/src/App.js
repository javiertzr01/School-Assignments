import React from "react";
import logo from "./logo.svg";
import "./App.css";

export default function App() {
    return (
        <div className="form-container">
            <form className="form">
				Test
				<br></br>
                <input
                    // onChange={(event) => {
                    //     setValues({ ...values, firstName: event.target.value });
                    // }}
                    // value={values.firstName}
                    id="first-name"
                    class="form-field"
                    type="text"
                    placeholder="First Name"
                    name="firstName"
                />
            </form>
        </div>
    );
}
