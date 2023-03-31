import React, { useState, useEffect, useRef } from 'react';

const ChatInput = ({ onSendMessage }) => {
  const [message, setMessage] = useState('');
  const textareaRef = useRef(null);

  const handleSubmit = (e) => {
    e.preventDefault();

    // Prevent sending empty messages
    if (message.trim() === '') return;

    onSendMessage(message);
    setMessage('');
  };

  const handleKeyPress = (e) => {
    // Create a new line when pressing Shift+Enter
    if (e.key === 'Enter' && e.shiftKey) {
      setMessage((prevMessage) => prevMessage + '\n');
      e.preventDefault();
    }
    // Send message when pressing Enter without Shift key
    else if (e.key === 'Enter') {
      handleSubmit(e);
    }
  };

  // Auto-resize the textarea
  useEffect(() => {
    textareaRef.current.style.height = 'inherit';
    textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
    textareaRef.current.scrollTop = textareaRef.current.scrollHeight;
  }, [message]);

  return (
    <div className="text-white mt-auto p-4 bg-bgblack">
      <form onSubmit={handleSubmit} className="w-full flex justify-center">
        <textarea
          ref={textareaRef}
          className="border-[1px] border-bglight bg-bgblack rounded-md shadow-md w-6/12 py-2 px-2 focus:outline-none resize-none"
          id="text-input"
          value={message}
          rows="1"
          style={{ maxHeight: '100px', overflowY: 'auto' }}
          onChange={(e) => setMessage(e.target.value)}
          onKeyPress={handleKeyPress}
        ></textarea>
      </form>
    </div>
  );
};

export default ChatInput;
