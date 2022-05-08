import React, { useState } from "react";

function SignUp() {
    const [user, setUser] = useState({ username: "", password: "" });

    const updateForm = (e) => {
        const { value, name } = e.target;

        setUser({ ...user, [name]: value });
    };

    const signup = (e) => {
        e.preventDefault();
        return false;
    }

    return (
        <form onSubmit={signup} className="flex items-center h-screen bg-sky-300">
            <div className="flex flex-col items-center w-full">
                <h1 className="text-5xl">Signup</h1>
                <div className="flex justify-between my-4 flex-col w-1/3">
                    <label htmlFor="username">Username:</label>
                    <input type="text" placeholder="John Doe" name="username"
                        onChange={updateForm} value={user.username} className="border-2 border-cyan-600 focus:border-green-400
                        outline-none w-full rounded-md p-2"/>
                </div>
                <div className="flex justify-between my-4 flex-col w-1/3">
                    <label htmlFor="password">Password:</label>
                    <input type="password" placeholder="" name="password" value={user.password} onChange={updateForm}
                        className="border-2 border-cyan-600 focus:border-green-400 outline-none w-full rounded-md p-2"/>
                </div>
                <footer className="flex justify-center">
                    <button onClick={signup} className="bg-green-400 rounded-md mt-4 py-3 px-10 text-white font-bold m-4">Signup</button>
                </footer>

            </div>
        </form>
    );
}

export default SignUp;