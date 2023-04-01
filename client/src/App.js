import React, { useState } from 'react';
import Sidebar from "./components/Sidebar/Sidebar"
import Main from "./components/Main/Main"

import Settings from "./components/Settings/Settings"

function App() {
  const [selectedRoom, setSelectedRoom] = useState('farnam');

  const handleRoomSelect = (roomId) => {
    setSelectedRoom(roomId);
  };

    return (
      <>
      <div className="font-vietnam flex h-screen">
      <Sidebar selectedRoom={selectedRoom} onRoomSelect={handleRoomSelect} />
      <Main selectedRoom={selectedRoom} />
      <Settings selectedRoom={selectedRoom}/>
    </div>
    </>
  )
}

export default App;
