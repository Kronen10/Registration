function signup(log,pass) {
    options = {
    method: 'POST',
    headers: {'Content-Type':'application/json;charset=utf-8'},
    body: JSON.stringify({"login": log, "password": pass})
    };
    
    fetch('http://localhost:8080/greeting', options)
    
    }