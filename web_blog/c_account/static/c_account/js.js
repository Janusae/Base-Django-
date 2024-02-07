const form = document.querySelector("form");
const firstName = document.querySelector("#firstName");
const lastName = document.querySelector("#lastName");
const email = document.querySelector("#email");
const password = document.querySelector("#password");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  checkInputs();
});

function checkInputs() {
  const firstNameValue = firstName.value.trim();
  const lastNameValue = lastName.value.trim();
  const emailValue = email.value.trim();
  const passwordValue = password.value.trim();

  if (firstNameValue === "") {
    setError(firstName, "First input can't be empty");
  } else if (!inputValidity(firstNameValue, "name")) {
    setError(firstName, "First name is invalid");
  } else {
    setSuccess(firstName);
  }

  if (lastNameValue === "") {
    setError(lastName, "Last name can't be empty");
  } else if (!inputValidity(lastNameValue, "name")) {
    setError(lastName, "Last name is invalid");
  } else {
    setSuccess(lastName);
  }

  if (emailValue === "") {
    setError(email, "Email can't be empty");
  } else if (!inputValidity(emailValue, "email")) {
    setError(email, "Email is invalid");
  } else {
    setSuccess(email);
  }

  if (passwordValue === "") {
    setError(password, "Password can't be empty");
  } else if (!inputValidity(passwordValue, "password")) {
    setError(password, "Password is invalid");
  } else {
    setSuccess(password);
  }
}

function setError(element, message) {
  const formControl = element.parentElement;
  const small = formControl.querySelector("small");

  formControl.className = "form-control error";
  small.innerText = message;
}
function setSuccess(element) {
  const formControl = element.parentElement;
  formControl.className = "form-control success";
}

function inputValidity(inputValue, inputName) {
  if (inputName === "name") {
    if (inputValue.length < 3) {
      return false;
    }
    return true;
  }

  if (inputName === "email") {
    return /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(inputValue);
  }

  if (inputName === "password") {
    console.log(inputValue);
    return /[a-zA-Z0-9]{6,10}/.test(inputValue);
  }
}
