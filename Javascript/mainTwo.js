// Biblioteca que faz a requisicao da aula passada com menos codigo
axios.get('https://api.github.com/users/foxtryan')
	.then(function(response){
		console.log(response);
	})
	.catch(function(error){
		console.warn(error);
	});
	
	