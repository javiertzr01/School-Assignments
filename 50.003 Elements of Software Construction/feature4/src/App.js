import React from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { Container, Row, Col, Form } from "react-bootstrap";

// TODO:
// Check wrapper

export default function App() {
    return (
        <Container>
            <Form>
                General Form
                <Row className="form-container">
                    {/* Primary Guest Row */}
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
                                type="text"
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



                <div className="customer">customer</div>
                <div className="payment">payment</div>
                <div className="summary">summary</div>
            </Form>
        </Container>
    );
}
