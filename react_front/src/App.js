import Join from "pages/Join";
import Login from "pages/Login";
import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { StoreProvider } from "stores/RootStore";

const App = () => {
  return (
    <StoreProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/join" element={<Join />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </BrowserRouter>
    </StoreProvider>
  );
};

export default App;
