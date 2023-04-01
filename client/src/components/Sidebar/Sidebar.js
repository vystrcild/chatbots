import React from 'react';
import ChatRoomSelector from './ChatRoomSelector';

const Sidebar = ({ onRoomSelect, selectedRoom }) => {




  return (
    <aside className="h-full w-2/12 bg-bgblack p-4 shadow text-white border-r-[1px] border-white border-opacity-25">

      <ChatRoomSelector selectedRoom={selectedRoom} onSelectRoom={onRoomSelect} />


    </aside>
  );
};

export default Sidebar;
