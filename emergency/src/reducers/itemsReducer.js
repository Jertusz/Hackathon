const initialState = {
  items: []
};

export default (state = initialState, action) => {
  switch (action.type) {
    case "LOAD_ITEMS":
      return {
        ...state,
        items: action.payload
      };
    default:
      return state;
  }
};
