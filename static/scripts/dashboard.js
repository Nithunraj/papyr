const titleInput = document.querySelector(".view-transaction-title");
const walletSelect = document.querySelector(".view-transaction-wallet");
const categorySelect = document.querySelector(".view-transaction-categories");
const descriptionInput = document.querySelector(".view-transaction-description");
const amountInput = document.querySelector(".view-transaction-amount");
const transactionInput = document.querySelector(".transaction_type_view");
const incomeButtonView = document.querySelector(".incomeButtonView");
const expenseButtonView = document.querySelector(".expenseButtonView");
const dateField = document.querySelector(".transaction_date")

function openTransactionPopup(transactionId, title, walletId, categoryId, title, description, amount, transactionType, transactionId, transactionDate) {
    document.getElementById("transaction_id").value=transactionId;

    const saveButtonViewDescription = document.querySelector(".save-view-button-close");
    saveButtonViewDescription.innerHTML = "Edit";
    saveButtonViewDescription.type = "button";
    const editTransactionHeader = document.querySelector(".view_transactions_header");
    editTransactionHeader.innerHTML = "View Transaction";

    saveButtonViewDescription.classList.remove("save-mode");

    document.getElementById("transactionModal").classList.add("active");

    titleInput.value = title;
    titleInput.readOnly = true;

    walletSelect.value = walletId;

    categorySelect.value = categoryId;

    descriptionInput.value = description;
    descriptionInput.readOnly = true;

    amountInput.value = amount;
    amountInput.readOnly = true;

    transactionInput.value = transactionType;

    if (transactionType === "income") {
        incomeButtonView.classList.add("income");
        expenseButtonView.classList.remove("expense");
    } else {
        incomeButtonView.classList.remove("income");
        expenseButtonView.classList.add("expense");
    };

    djangoDate = transactionDate.replace(", midnight", "");
    const dateObj = new Date(djangoDate);
    const formattedDate = dateObj.toISOString().split("T")[0];
    
    dateField.value = formattedDate;
    dateField.readOnly = true;

    walletSelect.disabled = true;
    categorySelect.disabled = true;
    incomeButtonView.disabled = true;
    expenseButtonView.disabled = true;
}

function toggleEditSave(btn) {
  const row = btn.closest("tr");   // current row only

  if (btn.textContent.trim() === "Edit") {
    btn.textContent = "Update";
    const editTransactionHeader = document.querySelector(".view_transactions_header");
    editTransactionHeader.innerHTML = "Edit Transaction";
    btn.classList.add("save-mode");

    titleInput.readOnly = false;
    walletSelect.disabled = false;
    categorySelect.disabled = false;
    incomeButtonView.disabled = false;
    expenseButtonView.disabled = false;
    dateField.readOnly = false;
  }
  else {
    const form = document.getElementById("demoForm");
    if (!form.checkValidity()) {
      form.reportValidity();
      return;               
    }
    btn.type = "submit";
    btn.closest("form").submit();
  }
}


const ModalEditTransactions = {
  open() {
    document.getElementById("transactionModal").classList.add("active");
  },
  close() {
    document.getElementById("transactionModal").classList.remove("active");
    Form.clearFields();

    const saveButtonViewDescription = document.querySelector(".save-view-button-close");
    saveButtonViewDescription.innerHTML = "Edit";
    saveButtonViewDescription.type = "button";
    const editTransactionHeader = document.querySelector(".view_transactions_header");
    editTransactionHeader.innerHTML = "View Transaction";

    saveButtonViewDescription.classList.remove("save-mode");
  },
};

function toggleDateDropdown() {
  const dropdown = document.getElementById("date-dropdown");
  dropdown.style.display =
    dropdown.style.display === "block" ? "none" : "block";
}

function setDateRange(type) {
  const dateDisplay = document.getElementById("date-display");
  const picker = document.getElementById("custom-date-picker");

  picker.style.display = "none"; // hide by default

  let formattedDate = "";
  const today = new Date();

  if (type === "today") {
    formattedDate = formatSingleDate(today);
  }

  else if (type === "yesterday") {
    const y = new Date();
    y.setDate(today.getDate() - 1);
    formattedDate = formatSingleDate(y);
  }

  else if (type === "last7") {
    formattedDate = formatRange(6);
  }

  else if (type === "last30") {
    formattedDate = formatRange(29);
  }

  else if (type === "custom") {
    picker.style.display = "flex";
    return;
  }

  dateDisplay.textContent = formattedDate;
}

function setDateRange(type) {
  const labelMap = {
    today: "Today",
    yesterday: "Yesterday",
    last7: "Last 7 Days",
    last30: "Last 30 Days",
    custom: "Custom Date"
  };

  let formattedDate = labelMap[type];

  if (type === "custom") {
    document.getElementById("customDateModal").style.display = "block";
    document.getElementById("date-dropdown").style.display = "none";
    return;
  } else if (labelMap[type] == "Today"){
    const today = new Date();
    const month = today.toLocaleString("en-US", { month: "long" });
    const day = today.getDate();

    formattedDate = `${month}, ${day}`;
  } else if (labelMap[type] === "Yesterday") {
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);

    const month = yesterday
      .toLocaleString("en-US", { month: "long" });
    const day = yesterday.getDate();

    formattedDate = `${month}, ${day}`;
  } else if (labelMap[type] === "Last 7 Days") {
    const endDate = new Date();          // today
    const startDate = new Date();
    startDate.setDate(endDate.getDate() - 6);

    const sameYear = startDate.getFullYear() === endDate.getFullYear();

    const startDay = startDate.getDate();
    const startMonth = startDate.toLocaleString("en-US", { month: "short" });
    const startYear = startDate.getFullYear();

    const endDay = endDate.getDate();
    const endMonth = endDate.toLocaleString("en-US", { month: "short" });
    const endYear = endDate.getFullYear();

    if (sameYear) {
      formattedDate = `${startMonth} ${startDay} - ${endMonth} ${endDay}`;
    } else {
      formattedDate = `${startMonth} ${startDay}, ${startYear} - ${endMonth} ${endDay}, ${endYear}`;
    }
  } else if (labelMap[type] === "Last 30 Days") {
    const endDate = new Date();          // today
    const startDate = new Date();
    startDate.setDate(endDate.getDate() - 29); // last 30 days incl today

    const sameYear = startDate.getFullYear() === endDate.getFullYear();

    const startDay = startDate.getDate();
    const startMonth = startDate.toLocaleString("en-US", { month: "short" });
    const startYear = startDate.getFullYear();

    const endDay = endDate.getDate();
    const endMonth = endDate.toLocaleString("en-US", { month: "short" });
    const endYear = endDate.getFullYear();

    if (sameYear) {
      formattedDate = `${startMonth} ${startDay} - ${endMonth} ${endDay}`;
    } else {
      formattedDate = `${startMonth} ${startDay}, ${startYear} - ${endMonth} ${endDay}, ${endYear}`;
    }
  }

  document.getElementById("date-display").innerText = formattedDate;
  document.getElementById("date-dropdown").style.display = "none";

  // TODO: call API / filter transactions
  // fetchTransactions(type);
}


document.addEventListener("click", function (e) {
  const wrapper = document.querySelector(".date-wrapper");
  if (!wrapper.contains(e.target)) {
    document.getElementById("date-dropdown").style.display = "none";
  }
});

function closeCustomDate() {
  document.getElementById("customDateModal").style.display = "none";
}

function formatDateRange(start, end) {
  const sameYear = start.getFullYear() === end.getFullYear();

  const startDay = start.getDate();
  const startMonth = start.toLocaleString("en-US", { month: "short" });
  const startYear = start.getFullYear();

  const endDay = end.getDate();
  const endMonth = end.toLocaleString("en-US", { month: "short" });
  const endYear = end.getFullYear();

  if (sameYear) {
    return `${startMonth} ${startDay} - ${endMonth} ${endDay}`;
  }

  return `${startMonth} ${startDay}, ${startYear} - ${endMonth} ${endDay}, ${endYear}`;
}

function applyCustomDate() {
  const startVal = document.getElementById("customStartDate").value;
  const endVal = document.getElementById("customEndDate").value;

  if (!startVal || !endVal) {
    alert("Please select both dates");
    return;
  }

  const start = new Date(startVal);
  const end = new Date(endVal);

  document.getElementById("date-display").textContent =
    formatDateRange(start, end);

  closeCustomDate();
}