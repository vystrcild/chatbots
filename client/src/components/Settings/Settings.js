import React from 'react';

const Settings = ({ onClearChat, selectedRoom, socket }) => {
  return (
    <div>
      {/* Your other settings components */}
      <button onClick={onClearChat(selectedRoom)}>Clear</button>
    </div>
  );
};

export default Settings;
