var listElement = document.querySelector("#app ul");
var inputElement = document.querySelector("#app input");
var buttonElement = document.querySelector("#app button");


// AGORA USAMOS O LOCAL STORAGE PRA BUSCAR A LISTA
//var todos = [
//	'Fazer café',
//	'Estudar Javascript',
//	'Acessar Rocketseat'
//];
var todos = JSON.parse(localStorage.getItem('list_todos')) || [];

function renderTodos() {
		// Limpar lista pra não duplicar itens
		listElement.innerHTML = "";
		
		for (todo of todos){
			var todoElement = document.createElement('li');
			var todoText = document.createTextNode(todo);
			
			var linkElement = document.createElement('a');
			var linkText = document.createTextNode('Excluir');
			
			//buscar posição para remover 
			var pos = todos.indexOf(todo);
			linkElement.setAttribute('onclick', 'deleteTodo('+pos+')');
			
			linkElement.setAttribute('href', '#');
			linkElement.appendChild(linkText);
			
			todoElement.appendChild(todoText);
			todoElement.appendChild(linkElement);
			listElement.appendChild(todoElement);
		}
}

renderTodos();

function addTodo() {
	var todoText = inputElement.value;
	
	todos.push(todoText);
	inputElement.value = "";
	renderTodos();
	saveToStorage();
}

buttonElement.onclick = addTodo;

function deleteTodo(pos) {
	todos.splice(pos, 1);
	renderTodos();
	saveToStorage();
}

// Salvar no local storage, eh um arquivo de chave e valor sring
// entao precisa converter em string. Apos isso add func no add e delete
function saveToStorage() {
	localStorage.setItem('list_todos', JSON.stringify(todos));
}