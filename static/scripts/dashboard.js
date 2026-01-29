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