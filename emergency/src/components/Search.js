import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { Input, Form } from "reactstrap";
import { getItems } from "../actions/itemsAction";

export class Search extends Component {
  state = {
    search: ""
  };

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  submit = e => {
    e.preventDefault();
    this.props.getItems(this.state.search.split(" "));
  };

  render() {
    return (
      <Form onSubmit={this.submit}>
        <Input
          onChange={this.onChange}
          value={this.state.search}
          name="search"
        ></Input>
      </Form>
    );
  }
}

const mapStateToProps = state => ({});

const mapDispatchToProps = { getItems };

export default connect(mapStateToProps, mapDispatchToProps)(Search);
