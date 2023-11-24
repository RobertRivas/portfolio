import React from 'react';
import { Container } from 'react-bootstrap';
import './BackgroundPicture.css';
import BasicExample from "./navbar"; // Create this file in the same directory

const BackgroundPicture = () => {
    return (
        <div className="background-picture">
            <Container>
                <BasicExample />
            </Container>
        </div>
    );
};

export default BackgroundPicture;
