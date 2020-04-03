// xhr > Visualiza req em Rede no Inspetor 
var xhr = new XMLHttpRequest();

xhr.open('GET', 'http://api.github.com/users/foxtryan');
xhr.send(null);

xhr.onreadystatechange = function(){
	if (xhr.readyState === 4) {
		console.log(JSON.parse(xhr.responseText));
	}
}

// Promisses
var minhaPromise = function() {
	return new Promise(function(resolve, reject){
		var xhr = new XMLHttpRequest();
		xhr.open('GET', 'http://api.github.com/users/foxtryan');
		xhr.send(null);
		
		xhr.onreadystatechange = function(){
			if (xhr.readyState ===4){
				if (xhr.status ===200) {
					resolve(JSON.parse(xhr.responseText));
				} else {
					reject("Erro na requisição");
				}
			}
		}
	});
}

// Retorna 'pending' pois ainda não foi finalizada
// por estar esperando a resposta do servidor
var resultado = minhaPromise();
console.log(resultado);

// Por isso não se coloca em uma variavel e sim:
minhaPromise()
	.then(function(response) {
		console.log(response);
	})
	.catch(function(error) {
		console.warn(error);
	});