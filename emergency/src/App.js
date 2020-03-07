import React, { Component } from "react";

import "bootstrap/dist/css/bootstrap.min.css";
import { Container } from "reactstrap";

import { Provider } from "react-redux";
import store from "./store";

// Components
import Search from "./components/Search";
import Display from "./components/Display";

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <Container>
          <h1>App</h1>
          <Search />
          <Display />
        </Container>
      </Provider>
    );
  }
}

export default App;
