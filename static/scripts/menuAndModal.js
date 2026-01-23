const MobileMenu = {
  open() {
    document.querySelector("aside").classList.add("active");
  },
  close() {
    document.querySelector("aside").classList.remove("active");
  },
};

const Modal = {
  open() {
    document.getElementById("modalOverlay").classList.add("active");
  },
  close() {
    document.getElementById("modalOverlay").classList.remove("active");
    Form.clearFields();
  },
};

const Modal_incomes = {
  open(overlayFor) {
    if (overlayFor === "income") {
      document.getElementById("modalOverlayIncomes").classList.add("active");
    } else {
      document.getElementById("modalOverlayExpenses").classList.add("active");
    }
  },
  close(closeOverlayFor) {
    if (closeOverlayFor === "income") {
      document.getElementById("modalOverlayIncomes").classList.remove("active");
      Form.clearFields();
    } else {
      document.getElementById("modalOverlayExpenses").classList.remove("active");
      Form.clearFields();
    }
  },
};

// Display date (November, 24)
let today = new Date();
let dd = String(today.getDate()).padStart(2, "0");
let mm = String(today.getMonth() + 1).padStart(2, "0"); //January is 0!;
let yyyy = today.getFullYear();
today = dd + "/" + mm + "/" + yyyy;

let myDate;
function formatDate(str) {
  var parts = str.split("/").map(Number);
  myDate = new Date("20" + parts[2], parts[1] - 1, parts[0]);
  return myDate.toLocaleString([], { month: "long" });
}
myDate = today;
const dateDisplay = formatDate(myDate.toString()) + ", " + dd;

function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

document.getElementById("date-display").innerHTML =
  capitalizeFirstLetter(dateDisplay);
