import { Container } from 'react-bootstrap';
import './EditDistanceBackroundPicture.css';
import BasicExample from "./navbar"; // Create this file in the same directory

const  editDistanceBackgroundPicture = () => {
    return (
        <div className="background-picture">
            <Container>
                <BasicExample />
            </Container>
        </div>
    );
};

export default editDistanceBackgroundPicture;
