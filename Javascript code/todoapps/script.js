document.addEventListener("DOMContentLoaded", function () {//listener for run if dom udah load

  const submitForm = document.getElementById("form"); //mengambil id=from dimasukan ke variable submitForm

  submitForm.addEventListener("submit", function (event) {
    event.preventDefault(); // mencegah behavior asli yg otomatis refresh
    addTodo(); //memanggil fungsi addTodo
    makeTodo();
  });
});