import React, { useState, useEffect } from "react"
import calendar from "../assets/calendar-days-solid.svg"
import EnterTransaction from "../components/EnterTransaction";
import Plus from "../assets/plus";

function Home() {
    const [showTranscation, setShowTransaction] = useState(false);
    const [balance, setBalance] = useState(0);

    useEffect(() => {
        const runFetch = async () => {
            const response = await fetch("/api/balance")
            if (response.ok) {
                const json = await response.json();
                setBalance(json.balance);
            }
        };

        runFetch();
    }, []);

    return (
        <div className="bg-neutral-900 h-screen p-2">
            <header className="flex justify-between">
                <div className="text-neutral-200 flex bg-cyan-500 p-2 rounded-md">
                    <img src={calendar} alt="calendar" className="w-5"/>
                    <span className="block ml-4 px-10 text-xl">Calendar</span>
                </div>
                <div className="text-neutral-200 w-fit">Balance: {balance}</div>
            </header>

            { showTranscation && <EnterTransaction close={() => setShowTransaction(false)}/> }
            <button className="bg-green-400 rounded-md mt-4 py-3 px-8 text-white font-bold m-4 flex"
                onClick={() => setShowTransaction(true)}>
                <Plus/>
                <span className="block mx-4">Add Transaction</span>
            </button>

            <footer>

            </footer>
        </div>
    );
}

export default Home;