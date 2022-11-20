function create_table(body) {
	if (document.getElementById("tab") !== null) {
		document.getElementById('tab').remove();};
	let table = document.createElement('table');
	table.innerHTML = "<tr><td> ID </td><td> login </td><td> comment </td></tr>";
	document.body.append(table);
	table.setAttribute('border', 1);
	table.setAttribute('cellspacing', 0);
	table.setAttribute('id', 'tab');
	
		for (let i = 0; i < body['data'].length; i++) {
	let tr = document.createElement('tr'); 
	tr.innerHTML = "<td>"+ (i+1) +"</td><td>"+ body['data'][i]['login'] +" </td><td> "+ body['data'][i]['comment'] +"</td>"; 
	document.getElementById('tab').append(tr); 
};};

function show() {
fetch('http://localhost:8080/greeting')
.then((response) => {
return response.text();
	})
	.then((data) => {
	body = JSON.parse(data);
	create_table(body)
});
};

function send(log,comm) {
options = {
method: 'POST',
headers: {'Content-Type':'application/json;charset=utf-8'},
body: JSON.stringify({"login": log, "comment": comm})
};

fetch('http://localhost:8080/greeting', options)



}