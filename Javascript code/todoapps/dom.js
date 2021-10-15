const UNCOMPLETED_LIST_TODO_ID = "todos";// menampung id elemen Todo yang belum selesai
const COMPLETED_LIST_TODO_ID = "completed-todos";// menampung id elemen todo yang sudah dilakukan
function addTodo() {
  const uncompletedTODOList = document.getElementById(UNCOMPLETED_LIST_TODO_ID); //variable global menampung id elemen Todo yg belum selesai
  const textTodo = document.getElementById("title").value; //mendapatkan id title dan masukan ke variable textTodo
  const timestamp = document.getElementById("date").value;

  const todo = makeTodo(textTodo, timestamp);
  uncompletedTODOList.append(todo); // append memasukan textTodo dan timestamp pada variable todo

}
function makeTodo(data, timestamp, isCompleted) { //menambahkan 2 parameter agar pengulangan tidak sama

  const textTitle = document.createElement("h2");//membuat element menjadi h2 memasukan ke textTitle
  textTitle.innerText = data; // memberikan value pada textTitle

  const textTimestamp = document.createElement("p");
  textTimestamp.innerText = timestamp; // menambahkan value pada textTimestamp

  const textContainer = document.createElement("div");
  textContainer.classList.add("inner")
  textContainer.append(textTitle, textTimestamp);// memasukan textTitle dan timestamp ke textContainer

  const container = document.createElement("div");
  container.classList.add("item", "shadow")
  container.append(textContainer);

  if (isCompleted) {
    container.append(
      createUndoButton(),
      createTrashButton()
    );
  } else {
    container.append(createCheckButton()); // memanggil createcheckbutton pada function makeTodo
  }
  return container;

}
function createButton(buttonTypeClass, eventListener) {// membuat button todo sudah selesai
  const button = document.createElement("button");
  button.classList.add(buttonTypeClass);
  button.addEventListener("click", function (event) {// parameter addeventlistener akan bekerja saat di click
    eventListener(event);
  });
  return button;
}
function addTaskToCompleted(taskElement) {
  const taskTitle = taskElement.querySelector(".inner > h2").innerText; //menampilkan todo yg sudah ditandai sudah selesai
  const taskTimestamp = taskElement.querySelector(".inner > p").innerText;

  const newTodo = makeTodo(taskTitle, taskTimestamp, true); // membuat variable newTodo untuk menampung title san timestamp todo yg sudah selesai
  const listCompleted = document.getElementById(COMPLETED_LIST_TODO_ID); //mengambil id elemen COMPLETED_LIST_TODO_ID
  listCompleted.append(newTodo);
  taskElement.remove();// menghapus todo yang sudah dilakukan
}

function createCheckButton() {// menandai todo yg sudah selesai
  return createButton("check-button", function (event) {
    addTaskToCompleted(event.target.parentElement);
  });
}
function removeTaskFromCompleted(taskElement) {// menghapus todo yg sudah selesai
  taskElement.remove();
}
function createTrashButton() { //membuat button hapus todo
  return createButton("trash-button", function (event) {
    removeTaskFromCompleted(event.target.parentElement);
  });
}
function createUndoButton() {
  return createButton("undo-button", function (event) {
    undoTaskToCompleted(event.target.parentElement);//event.target.parentElement listener buat undo
  });
}
function undoTaskToCompleted(taskElement) {
  const listUncompleted = document.getElementById(UNCOMPLETED_LIST_TODO_ID);// mendapatkan id element UNCOMPLETED_LIST_TODO_ID
  const taskTitle = taskElement.querySelector(".inner > h2").innerText;
  const taskTimestamp = taskElement.querySelector(".inner > p").innerText;

  const newTodo = makeTodo(taskTitle, taskTimestamp, false);

  listUncompleted.append(newTodo);
  taskElement.remove();
}