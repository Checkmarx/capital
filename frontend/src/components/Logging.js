import React, { memo } from 'react';

function Logging() {
  return (
    <>
      <div
        style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          height: '100vh',
        }}
      >
        This app does not log and monitor anything. <br />
      </div>
    </>
  );
}

export default memo(Logging);
