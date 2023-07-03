<template>
 <div class="home">
   <h3>{{msg}}</h3>
 </div>
</template>

<script>
    export default {
        name:'Home',
        data(){
            return {
                msg:'这里是Home视图'
            }
        }
    }
</script>

<style scoped>
h3 {
  background-color: chocolate;
}
</style>
