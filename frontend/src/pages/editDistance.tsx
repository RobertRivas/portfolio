import React, {useState, useEffect} from "react";
import { Container, Form, Button } from 'react-bootstrap';
import EditDistanceBackground from "../components/EditDistanceBackround";



// interface ResponseData {
//     word_one: string;
//     word_two: string;
//     word_one_calc: string;
//     word_two_calc: string;
//     distance: string;
// }

export function EditDistance () {

    const [wordOne, setWordOne] = useState('');
    const [wordTwo, setWordTwo] = useState('');
    const [response, setResponse] = useState('');
    const [csrfToken, setCsrfToken] = useState('');

    useEffect(() => {
        const fetchCsrfToken = async () => {
            try {
                const response = await fetch('/api/csrf_cookie/');
                if (response.ok) {
                    setCsrfToken(response.headers.get('X-CSRFToken') || '');
                } else {
                    throw new Error('Failed to fetch CSRF token.');
                }
            } catch (error) {
                console.error(error);
            }
        };

        fetchCsrfToken();
    }, []);



    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        try {
            const response = await fetch('http://localhost:8000/editdistance/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify({ word_one: wordOne, word_two: wordTwo }),
            });

            const data = await response.json();
            setResponse(data);
            console.log(data);
        } catch (error) {
            console.error(error);
        }
    };


    return (

    <Container>
        <EditDistanceBackground  />

        <Form onSubmit={handleSubmit}>
            <Form.Group controlId="formWordOne">
                <Form.Label>Enter word one</Form.Label>
                <Form.Control
                    type="text"
                    placeholder="Word One"
                    name="word_one"
                    value={wordOne}
                    onChange={(e) => setWordOne(e.target.value)}
                />

                <Form.Label>Enter word two</Form.Label>
                <Form.Control
                    type="text"
                    placeholder="Word Two"
                    name="word_two"
                    value={wordTwo}
                    onChange={(e) => setWordTwo(e.target.value)}
                />
            </Form.Group>
            <Button variant="primary" type="submit">
                Submit
            </Button>
        </Form>
        <p>Response: {JSON.stringify(response)}</p>

    </Container>


);
}

export default EditDistance;















