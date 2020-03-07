import axios from "axios";

export const getItems = q => dispatch => {
  axios
    .get(
      "https://api.edamam.com/search?app_key=998d1837e99b9133559bd3adafb1c0af&app_id=8b586bbd&to=10&q=" +
        q
    )
    .then(res => dispatch({ type: "LOAD_ITEMS", payload: res.data }));
};
