<template>
  <div>
      <Header></Header>
      <Content> v-bind:propsdata="userList"</Content> <!-- 상위 -> 하위: props 속성, 하위 -> 상위: event emit 사용-->
      <Footer></Footer>
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import Content from "./components/Content.vue";
import Footer from "./components/Footer.vue";
import axios from "axios";

let url = "http://localhost:8000/";

export default {
  data: () => {
    return {
      userList: []
    };
  },
  components: {
    Header, // 이름 정하기 왜 안됨?
    Content,
    Footer,
  },
  mounted() {
    axios({
      method: "GET",
      url: url
    })
      .then(response => {
        this.userList = response.data;
      })
      .catch(response => {
        console.log("Failed", response)
      })
  },
  methods: {
    getUserList: function() {},
    updateUserList: function() {},
    deleteUserList: function() {}
  }
};
</script>

<style></style>