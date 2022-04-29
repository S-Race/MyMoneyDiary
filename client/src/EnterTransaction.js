import React, { useState } from "react";

import Modal from "./Modal";

const EnterTransaction = ({ close }) => {
    const [transaction, setTransaction] = useState({ amount: 0., details: "", type: "Deposit" });

    const updateTransaction = e =>
        setTransaction({ ...transaction, [e.target.name]: e.target.value });

    return (
        <Modal onClose={close} center>
            <div className="rounded-md text-neutral-800 bg-white md:w-3/5 w-full px-4 md:mx-0 mx-2">
                <header className="flex justify-between items-center py-4 border-b-2 border-neutral-100 mb-8">
                    <span className="text-xl font-bold">Enter a Transaction</span>
                    <span className="hover:text-red-600 text-4xl cursor-pointer" onClick={close}>&times;</span>
                </header>
                <div className="flex justify-between my-4 items-center">
                    <label htmlFor="transaction-amount" className="text-lg font-medium">Amount:</label>
                    <input type="number" step="0.01" min="0" value={transaction.amount} onChange={updateTransaction} name="amount"
                        placeholder="0.00" className="border-2 border-cyan-600 focus:border-green-400
                        outline-none w-3/4 rounded-md p-2"/>
                </div>
                <div className="flex justify-between my-4 items-center">
                    <label htmlFor="transaction-amount" className="text-lg font-medium">Details:</label>
                    <textarea className="border-2 border-cyan-600 focus:border-green-400 outline-none w-3/4
                        rounded-md p-2" placeholder="Enter Transaction Description">

                    </textarea>
                </div>
                <div className="flex justify-between my-4 items-center">
                    <label htmlFor="transaction-type" className="text-lg font-medium">Transaction type:</label>
                    <select name="transaction-type" id="transaction-type"
                        className="border-2 border-cyan-600 focus:border-green-400 outline-none rounded-md p-2">
                        <option value="Deposit">Deposit</option>
                        <option value="Withdraw">Withdraw</option>
                    </select>
                </div>
                <footer className="flex justify-center items-center">
                    <button className="bg-green-400 rounded-md mt-4 py-3 px-10 text-white font-bold m-4">Enter
                    </button>
                </footer>
            </div>
        </Modal>
    );
}

export default EnterTransaction;
