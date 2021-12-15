<template>
	<div>
    <ul>
      <li>{{ post.title }}</li>
    </ul>
	</div>
</template>

<script>
  export default {
    name: "Posts",
    props: {
      post: Object,
    },
  };
</script>