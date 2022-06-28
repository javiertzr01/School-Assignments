import React from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { Container, Row, Col, Form, Button } from "react-bootstrap";
import countryList from "react-select-country-list";
import { Formik } from "formik";
import * as yup from "yup";

let thisYear = new Date().getFullYear();
let yearList = [];
for (let i = 0; i < 21; i++) {
    yearList.push(thisYear + i);
}
let countryOptions = countryList().getLabels();

yup.setLocale({
    number:{
        default: "Please enter a valid handphone number"
    }
});

const schema = yup.object().shape({
    guestFirstName: yup.string().required("Please enter a first name"),
    guestLastName: yup.string().required("Please enter a last name"),
    guestHpNum: yup
        .number()
        .typeError("Please enter a valid handphone number")
        .integer("Invalid Number")
        .positive("Invalid Number")
        .required("Please enter your handphone number"),
    guestSpecialReq: yup.string(),
    customerFirstName: yup.string().required("Please enter a first name"),
    customerEmail: yup
        .string()
        .email("Please enter a valid email")
        .required("Please enter an email"),
    cardName: yup.string().required("Please enter a first name"),
    cardNumber: yup
        .number()
        .typeError("Please enter a valid card number")
        .integer("Invalid Card Number")
        .positive("Invalid Card Number")
        .required("Please enter a valid card number"),
    cardMonth: yup.string().required("Please choose a month"),
    cardYear: yup.string().required("Please choose a year"),
    cardCVC: yup
        .number()
        .typeError("Please enter a valid card CVC number")
        .integer("Invalid CVC number")
        .positive("Invalid CVC number")
        .required("Please enter a valid card CVC number"),
    billingAddress: yup.string().required("Please enter a billing address"),
    billingCity: yup.string().required("Please enter a city"),
    billingPostalCode: yup
        .number()
        .typeError("Please enter a valid postal code")
        .integer("Please enter a valid postal code")
        .positive("Please enter a valid postal code")
        .required("Please enter a valid postal code"),
    billingCountry: yup.string().required("Please choose a country"),
});

export default function App() {
    return (
        <Container>
            <Row>
                {/* Booking Summary */}
                <Col sm={true} md={{ order: "last" }} className="p-4">
                    <Row className="form-container mb-3">Booking Summary</Row>
                </Col>

                {/* Form */}
                <Col md={{ span: 8 }} className="p-4">
                    <Formik
                        validationSchema={schema}
                        onSubmit={(values, { setSubmitting }) => {
                            setTimeout(() => {
                                alert(JSON.stringify(values, null, 2));
                                setSubmitting(false);
                            }, 400);
                        }}
                        initialValues={{
                            guestFirstName: "",
                            guestLastName: "",
                            guestHpNum: "",
                            guestSpecialReq: "",
                            customerFirstName: "",
                            customerEmail: "",
                            cardName: "",
                            cardNumber: "",
                            cardMonth: "",
                            cardYear: "",
                            cardCVC: "",
                            billingAddress: "",
                            billingCity: "",
                            billingPostalCode: "",
                            billingCountry: "",
                        }}
                    >
                        {(formik) => (
                            <Form onSubmit={formik.handleSubmit}>
                                {/* Primary Guest*/}
                                <Row className="form-container mb-3">
                                    <Form.Label>Primary Guest</Form.Label>

                                    <Row className="mb-3">
                                        <Form.Group
                                            as={Col}
                                            sm={true}
                                            className="mb-3"
                                            controlId="firstName"
                                        >
                                            <Form.Label>First Name</Form.Label>
                                            <Form.Control
                                                type="text"
                                                placeholder="First Name"
                                                {...formik.getFieldProps(
                                                    "guestFirstName"
                                                )}
                                                isInvalid={
                                                    formik.touched
                                                        .guestFirstName &&
                                                    !!formik.errors
                                                        .guestFirstName
                                                }
                                            />
                                            <Form.Control.Feedback type="invalid">
                                                {formik.errors.guestFirstName}
                                            </Form.Control.Feedback>
                                        </Form.Group>

                                        <Form.Group
                                            as={Col}
                                            sm={true}
                                            className="mb-3"
                                            controlId="lastName"
                                        >
                                            <Form.Label>Last Name</Form.Label>
                                            <Form.Control
                                                type="text"
                                                placeholder="Last Name"
                                                {...formik.getFieldProps(
                                                    "guestLastName"
                                                )}
                                                isInvalid={
                                                    formik.touched
                                                        .guestLastName &&
                                                    !!formik.errors
                                                        .guestLastName
                                                }
                                            />
                                            <Form.Control.Feedback type="invalid">
                                                {formik.errors.guestLastName}
                                            </Form.Control.Feedback>
                                        </Form.Group>

                                        <Form.Group
                                            as={Col}
                                            sm={true}
                                            className="mb-3"
                                            controlId="hpNum"
                                        >
                                            <Form.Label>
                                                Phone Number
                                            </Form.Label>
                                            <Form.Control
                                                type="text"
                                                placeholder="Number"
                                                {...formik.getFieldProps(
                                                    "guestHpNum"
                                                )}
                                                isInvalid={
                                                    formik.touched.guestHpNum &&
                                                    !!formik.errors.guestHpNum
                                                }
                                            />
                                            <Form.Control.Feedback type="invalid">
                                                {formik.errors.guestHpNum}
                                            </Form.Control.Feedback>
                                        </Form.Group>
                                    </Row>
                                    <Row className="mb-3">
                                        <Form.Label>Special Request</Form.Label>
                                        <Form.Group>
                                            <Form.Control
                                                as="textArea"
                                                style={{ resize: "none" }}
                                                type="text"
                                                placeholder="Write your special requests here"
                                                maxlength={250}
                                                rows={3}
                                                {...formik.getFieldProps(
                                                    "guestSpecialReq"
                                                )}
                                            />
                                        </Form.Group>
                                    </Row>
                                </Row>
                                {/* Your Details */}
                                <Row className="form-container mb-3">
                                    <Form.Label>Your Details</Form.Label>
                                    <Row className="mb-3">
                                        <Form.Group
                                            as={Col}
                                            sm={true}
                                            className="mb-3"
                                            controlId="customerName"
                                        >
                                            <Form.Label>First Name</Form.Label>
                                            <Form.Control
                                                type="text"
                                                placeholder="First Name"
                                                {...formik.getFieldProps(
                                                    "customerFirstName"
                                                )}
                                                isInvalid={
                                                    formik.touched
                                                        .customerFirstName &&
                                                    !!formik.errors
                                                        .customerFirstName
                                                }
                                            />
                                            <Form.Control.Feedback type="invalid">
                                                {
                                                    formik.errors
                                                        .customerFirstName
                                                }
                                            </Form.Control.Feedback>
                                        </Form.Group>

                                        <Form.Group
                                            as={Col}
                                            sm={true}
                                            className="mb-3"
                                            controlId="customerEmail"
                                        >
                                            <Form.Label>
                                                Email Address
                                            </Form.Label>
                                            <Form.Control
                                                type="email"
                                                placeholder="Email"
                                                {...formik.getFieldProps(
                                                    "customerEmail"
                                                )}
                                                isInvalid={
                                                    formik.touched
                                                        .customerEmail &&
                                                    !!formik.errors
                                                        .customerEmail
                                                }
                                            />
                                            <Form.Control.Feedback type="invalid">
                                                {formik.errors.customerEmail}
                                            </Form.Control.Feedback>
                                        </Form.Group>
                                    </Row>
                                </Row>
                                {/* Payment Information*/}
                                <Row className="form-container mb-3">
                                    {/* Card Details */}
                                    <Form.Label>Payment Information</Form.Label>
                                    <Row className="mb-3">
                                        {/* Card Details 1st Row*/}
                                        <Form.Group
                                            as={Col}
                                            sm={true}
                                            className="mb-3"
                                            controlId="cardName"
                                        >
                                            <Form.Label>
                                                Name on Card
                                            </Form.Label>
                                            <Form.Control
                                                type="text"
                                                {...formik.getFieldProps(
                                                    "cardName"
                                                )}
                                                isInvalid={
                                                    formik.touched.cardName &&
                                                    !!formik.errors.cardName
                                                }
                                            />
                                            <Form.Control.Feedback type="invalid">
                                                {formik.errors.cardName}
                                            </Form.Control.Feedback>
                                        </Form.Group>

                                        <Form.Group
                                            as={Col}
                                            sm={true}
                                            className="mb-3"
                                            controlId="cardNumber"
                                        >
                                            <Form.Label>Card Number</Form.Label>
                                            <Form.Control
                                                type="text"
                                                // pattern="\d*"
                                                maxlength="16"
                                                {...formik.getFieldProps(
                                                    "cardNumber"
                                                )}
                                                isInvalid={
                                                    formik.touched.cardNumber &&
                                                    !!formik.errors.cardNumber
                                                }
                                            />
                                            <Form.Control.Feedback type="invalid">
                                                {formik.errors.cardNumber}
                                            </Form.Control.Feedback>
                                        </Form.Group>
                                    </Row>

                                    <Row className="mb-3">
                                        {/* Card Details 2nd Row*/}
                                        <Form.Group
                                            as={Col}
                                            md={true}
                                            className="mb-3"
                                            controlId="cardExpiry"
                                        >
                                            <Row>
                                                <Form.Label>
                                                    Expiry Date
                                                </Form.Label>
                                            </Row>
                                            <Row>
                                                <Col sm={true}>
                                                    <Form.Select
                                                        className="mb-3"
                                                        aria-label="cardMonth"
                                                        {...formik.getFieldProps(
                                                            "cardMonth"
                                                        )}
                                                        isInvalid={
                                                            formik.touched
                                                                .cardMonth &&
                                                            formik.values
                                                                .cardMonth ===
                                                                ""
                                                        }
                                                    >
                                                        <option
                                                            value=""
                                                            disabled
                                                            selected
                                                        >
                                                            Month
                                                        </option>
                                                        <option value="jan">
                                                            January
                                                        </option>
                                                        <option value="feb">
                                                            February
                                                        </option>
                                                        <option value="mar">
                                                            March
                                                        </option>
                                                        <option value="apr">
                                                            April
                                                        </option>
                                                        <option value="may">
                                                            May
                                                        </option>
                                                        <option value="jun">
                                                            June
                                                        </option>
                                                        <option value="jul">
                                                            July
                                                        </option>
                                                        <option value="aug">
                                                            August
                                                        </option>
                                                        <option value="sep">
                                                            September
                                                        </option>
                                                        <option value="oct">
                                                            October
                                                        </option>
                                                        <option value="nov">
                                                            November
                                                        </option>
                                                        <option value="dec">
                                                            December
                                                        </option>
                                                    </Form.Select>
                                                    <Form.Control.Feedback type="invalid">
                                                        {
                                                            formik.errors
                                                                .cardMonth
                                                        }
                                                    </Form.Control.Feedback>
                                                </Col>
                                                <Col sm={true}>
                                                    <Form.Select
                                                        className="mb-3"
                                                        aria-label="cardYear"
                                                        {...formik.getFieldProps(
                                                            "cardYear"
                                                        )}
                                                        isInvalid={
                                                            formik.touched
                                                                .cardYear &&
                                                            formik.values
                                                                .cardMonth ===
                                                                ""
                                                        }
                                                    >
                                                        <option
                                                            value=""
                                                            disabled
                                                            selected
                                                        >
                                                            Year
                                                        </option>
                                                        {yearList.map(
                                                            (year, index) => {
                                                                return (
                                                                    <option
                                                                        value={
                                                                            year
                                                                        }
                                                                    >
                                                                        {year}
                                                                    </option>
                                                                );
                                                            }
                                                        )}
                                                    </Form.Select>
                                                    <Form.Control.Feedback type="invalid">
                                                        {formik.errors.cardYear}
                                                    </Form.Control.Feedback>
                                                </Col>
                                            </Row>
                                        </Form.Group>

                                        <Form.Group
                                            as={Col}
                                            md={true}
                                            className="mb-3"
                                            controlId="cardCVC"
                                        >
                                            <Form.Label>CVV/CVC</Form.Label>
                                            <Form.Control
                                                type="text"
                                                // pattern="\d*"
                                                maxlength="4"
                                                {...formik.getFieldProps(
                                                    "cardCVC"
                                                )}
                                                isInvalid={
                                                    formik.touched.cardCVC &&
                                                    !!formik.errors.cardCVC
                                                }
                                            />
                                            <Form.Control.Feedback type="invalid">
                                                {formik.errors.cardCVC}
                                            </Form.Control.Feedback>
                                        </Form.Group>
                                    </Row>

                                    {/*Billing Address*/}
                                    <Form.Label>Billing Address</Form.Label>
                                    {/* Billing Address 1st Row */}
                                    <Row>
                                        {/* Address */}
                                        <Form.Group
                                            as={Col}
                                            md={true}
                                            className="mb-3"
                                            controlId="billingAddress"
                                        >
                                            <Form.Label>Address</Form.Label>
                                            <Form.Control
                                                type="text"
                                                {...formik.getFieldProps(
                                                    "billingAddress"
                                                )}
                                                isInvalid={
                                                    formik.touched
                                                        .billingAddress &&
                                                    !!formik.errors
                                                        .billingAddress
                                                }
                                            ></Form.Control>
                                            <Form.Control.Feedback type="invalid">
                                                {formik.errors.billingAddress}
                                            </Form.Control.Feedback>
                                        </Form.Group>
                                        {/* City */}
                                        <Form.Group
                                            as={Col}
                                            md={true}
                                            className="mb-3"
                                            controlId="billingCity"
                                        >
                                            <Form.Label>City</Form.Label>
                                            <Form.Control
                                                type="text"
                                                {...formik.getFieldProps(
                                                    "billingCity"
                                                )}
                                                isInvalid={
                                                    formik.touched
                                                        .billingCity &&
                                                    !!formik.errors.billingCity
                                                }
                                            ></Form.Control>
                                            <Form.Control.Feedback type="invalid">
                                                {formik.errors.billingCity}
                                            </Form.Control.Feedback>
                                        </Form.Group>
                                    </Row>

                                    {/* Billing Address 2nd Row */}
                                    <Row>
                                        {/* Postal Code */}
                                        <Form.Group
                                            as={Col}
                                            md={true}
                                            className="mb-3"
                                            controlId="billingPostalCode"
                                        >
                                            <Form.Label>Postal Code</Form.Label>
                                            <Form.Control
                                                type="text"
                                                {...formik.getFieldProps(
                                                    "billingPostalCode"
                                                )}
                                                isInvalid={
                                                    formik.touched
                                                        .billingPostalCode &&
                                                    !!formik.errors
                                                        .billingPostalCode
                                                }
                                            ></Form.Control>
                                            <Form.Control.Feedback type="invalid">
                                                {
                                                    formik.errors
                                                        .billingPostalCode
                                                }
                                            </Form.Control.Feedback>
                                        </Form.Group>
                                        {/* Country */}
                                        <Form.Group
                                            as={Col}
                                            md={true}
                                            className="mb-3"
                                            controlId="billingCountry"
                                        >
                                            <Form.Label>Country</Form.Label>
                                            <Form.Select
                                                className="mb-3"
                                                aria-label="billingCountry"
                                                // value={countryValue}
                                                // onChange={billingCountryHandler}
                                                {...formik.getFieldProps(
                                                    "billingCountry"
                                                )}
                                                isInvalid={
                                                    formik.touched.billingCountry &&
                                                    formik.values.billingCountry ===
                                                        ""
                                                }
                                            >
                                                <option
                                                    value=""
                                                    disabled
                                                    selected
                                                > </option>
                                                {countryOptions.map(
                                                    (country, index) => {
                                                        return (
                                                            <option
                                                                value={country}
                                                            >
                                                                {country}
                                                            </option>
                                                        );
                                                    }
                                                )}
                                            </Form.Select>
                                            <Form.Control.Feedback type="invalid">
                                                {
                                                    formik.errors
                                                        .billingCountry
                                                }
                                            </Form.Control.Feedback>
                                        </Form.Group>
                                    </Row>
                                </Row>
                                {/* Submit Button */}
                                <Row className="mb-5">
                                    <Col
                                        lg={{ span: 10, offset: 1 }}
                                        className="d-grid gap-2"
                                    >
                                        <Button
                                            variant="danger"
                                            type="submit"
                                            size="lg"
                                        >
                                            Confirm Booking
                                        </Button>
                                    </Col>
                                </Row>
                            </Form>
                        )}
                    </Formik>
                </Col>
            </Row>
        </Container>
    );
}
