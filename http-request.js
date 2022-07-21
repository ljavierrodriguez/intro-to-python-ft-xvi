fetch('https://jsonplaceholder.typicode.com/users', {
    method: 'GET', // GET, POST, PUT, DELETE
    // body: JSON.stringify(info): , // POST, PUT
    headers: {
        'Content-Type': 'application/json'
    }
})
    .then((response) => {
        // respuesta del servidor
        return response.json()
    })
    .then((data) => {
        console.log(data);
    })
    .catch((error) => {
        console.log(error)
    })


person = {
    name: 'Luis',
    lastname: 'Rodriguez'
}

person.name
person['name']