import React from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { Container, Row, Col, Form } from "react-bootstrap";

export default function App() {
    return (
        <Container>
            <Form>
                General Form
                <Row className="form-container mb-3">
                    {/* Primary Guest*/}
                    <Form.Label>Primary Guest</Form.Label>


                    <Row className="mb-3">
                        <Form.Group as={Col} sm={true} className="mb-3" controlId="firstName">
                            <Form.Label>First Name</Form.Label>
                            <Form.Control
                                type="text"
                                placeholder="First Name"
                            />
                        </Form.Group>


                        <Form.Group as={Col} sm={true} className="mb-3" controlId="lastName">
                            <Form.Label>Last Name</Form.Label>
                            <Form.Control type="text" placeholder="Last Name" />
                        </Form.Group>


                        <Form.Group as={Col} sm={true} className="mb-3" controlId="hpNum">
                            <Form.Label>Phone Number</Form.Label>
                            <Form.Control
                                type="number"
                                placeholder="Number"
                            />
                        </Form.Group>


                    </Row>
                    <Row className="mb-3">
                        <Form.Label>Special Request</Form.Label>
                        <Form.Group>
                            <Form.Control 
                                as="textArea"
                                style={{resize: "none"}}
                                type="text"
                                placeholder="Write your special requests here"
                                maxlength={250}
                                rows={3}
                            />
                        </Form.Group>
                    </Row>
                </Row>


                
                <Row className="form-container mb-3">
                    {/* Your Details */}
                    <Form.Label>Your Details</Form.Label>
                    <Row className="mb-3">
                        <Form.Group as={Col} sm={true} className="mb-3" controlId="customerName">
                            <Form.Label>First Name</Form.Label>
                            <Form.Control
                                type="text"
                                placeholder="First Name"
                            />
                        </Form.Group>


                        <Form.Group as={Col} sm={true} className="mb-3" controlId="customerEmail">
                            <Form.Label>Email Address</Form.Label>
                            <Form.Control type="email" placeholder="Email" />
                        </Form.Group>
                    </Row>

                </Row>
                
                <Row className="form-container mb-3">
                    {/* Payment Information*/}
                    <Form.Label>Payment Information</Form.Label>
                    <Row className="mb-3">
                        {/* Card Details 1st Row*/}
                        <Form.Group as={Col} sm={true} className="mb-3" controlId="cardName">
                            <Form.Label>Name on Card</Form.Label>
                            <Form.Control
                                type="text"
                            />
                        </Form.Group>

                        <Form.Group as={Col} sm={true} className="mb-3" controlId="cardNumber">
                            <Form.Label>Card Number</Form.Label>
                            <Form.Control
                                type="text"
                                pattern="\d*"
                                maxlength="16"
                            />
                        </Form.Group>
                    </Row>


                    <Row className="mb-3">
                        {/* Card Details 2nd Row*/}
                        <Form.Group as={Col} sm={true} className="mb-3" controlId="cardExpiry">
                        <Form.Label>Expiry Date</Form.Label>
                            {/* TODO: Include Expiry Date Info*/}
                        </Form.Group>

                        <Form.Group as={Col} sm={true} className="mb-3" controlId="cardCVC">
                            <Form.Label>CVV/CVC</Form.Label>
                            <Form.Control
                                type="text"
                                pattern="\d*"
                                maxlength="4"
                            />
                        </Form.Group>
                    </Row>

                    {/*Billing Address*/}
                    <Form.Label>Billing Address</Form.Label>

                </Row>
                <div className="summary">summary</div>
            </Form>
        </Container>
    );
}
