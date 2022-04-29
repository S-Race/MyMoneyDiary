import React from "react";

import money_bag from "./assets/Money_Bag_Emoji_grande.png";

const SplashScreen = () => {
    return (
        <div className="flex justify-center items-center bg-neutral-900 h-screen">
            <h1 className="text-6xl text-white">My Money Diary</h1>
            <img src={money_bag} alt=""></img>
            <h4 className="text-white">Todays Entry</h4>
        </div>
    );
};

export default SplashScreen;