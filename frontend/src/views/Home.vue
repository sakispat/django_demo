<template>
  <div>
    <Posts v-for="post in listPosts"
      v-bind:key="post.id" v-bind:post="post"
    />
    <img src="../assets/python-book.jpeg" alt="Python Book">
  </div>
</template>

<script>
  import axios from "axios";
  import Posts from "@/components/Posts.vue";

  export default {
    name: "Home",
    data(){
      return {
        listPosts: [],
      }
    },
    components: {
      Posts,
    },
    methods: {
      async getListPosts(){
        const path = 'api/posts/';
        await axios.get(path).then((res) => {
          console.log(res.data);
          this.listPosts = res.data;
        }).catch((err) => {
          console.log(err);
        });
      },
    },
    mounted(){
      this.getListPosts();
    },
  };
</script>

<style scoped>
  img {
    width: 30%;
    height: auto;
  }
</style>