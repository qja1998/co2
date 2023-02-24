<template>
  <div>
      <Header></Header>
      <Content></Content>
      <Footer></Footer>
  </div>
</template>

<script>
import Header from "./components/Header.vue"
import Content from "./components/Content.vue"
import Footer from "./components/Footer.vue"

export default {
  data: function() {
    return {
      name: "leffept"
    };
  },
  components: {
    Header,
    Content,
    Footer,
  },
};
</script>

<style></style>