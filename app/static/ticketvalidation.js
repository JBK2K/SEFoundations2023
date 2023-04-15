const mainNumbers = document.querySelectorAll('[name^="main"]');
for (let i = 0; i < mainNumbers.length; i++) {
  mainNumbers[i].addEventListener("change", function (event) {
    // Get the value of the changed input
    const newValue = event.target.value;

    // Check if the new value is already used in another input
    for (let j = 0; j < mainNumbers.length; j++) {
      if (j !== i && mainNumbers[j].value === newValue) {
        alert(
          "Main numbers cannot be repeated. Please choose a different number."
        );
        event.target.value = ""; // Reset the changed input to an empty value
        break;
      }
    }
  });
}
const superNumbers = document.querySelectorAll('[name^="super"]');
for (let i = 0; i < superNumbers.length; i++) {
  superNumbers[i].addEventListener("change", function (event) {
    // Get the value of the changed input
    const newValue = event.target.value;

    // Check if the new value is already used in another input
    for (let j = 0; j < superNumbers.length; j++) {
      if (j !== i && superNumbers[j].value === newValue) {
        alert(
          "Super numbers cannot be repeated. Please choose a different number."
        );
        event.target.value = ""; // Reset the changed input to an empty value
        break;
      }
    }
  });
}

// check that numbers are not larger as 50 and 12 for main and super numbers
