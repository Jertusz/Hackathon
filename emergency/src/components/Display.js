import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import { ListGroup, ListGroupItem, Card, CardBody, CardImg } from "reactstrap";

export class Display extends Component {
  render() {
    const { items } = this.props;
    return (
      <Fragment>
        {items &&
          items.hits &&
          items.hits.map(hit => (
            <Card key={hit.recipe.uri}>
              <CardImg src={hit.recipe.image}></CardImg>
              <CardBody>
                <a href={hit.recipe.url}>{hit.recipe.label}</a>
              </CardBody>
            </Card>
          ))}
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  items: state.items.items
});

const mapDispatchToProps = {};

export default connect(mapStateToProps, mapDispatchToProps)(Display);
