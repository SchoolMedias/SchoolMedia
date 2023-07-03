<template>
  <div class="content mt-7 pt-5">
    <h1>This is DataTest</h1>
    {{d2}}
    <p v-for="d in d1">
      {{d}}
    </p>
    <button @click="init">点击获取数据</button>
    <div style="margin-top: 50px">
      <input id="search" name="search" ref="keywords">
      <button @click="search">搜索</button>
      <p style="color: black;margin-top: 10px">{{d3}}</p>
  </div>
  </div>

</template>

<script src="../assets/js/jquery-3.2.1.min.js"></script> <!--引入外部js-->
<script>
    export default {
        name: "DataTest",
        data:function(){
            return {
                d1:['默认列表数据1','默认列表数据2'],
                d2:'默认字符串',
                d3:'数据展示',
            }
        },
        methods:{
            init:function () {
                let _this = this;
                this.$http.request({
                    url:_this.$url+'DataTest/',
                    method:"get",
                }).then(function (response) {
                    console.log(response);
                    _this.d1 = response.data
                }).catch(function (response) {
                    console.log(response)
                })
            },
            search:function () {
                let _this = this;
                let val = _this.$refs.keywords.value;
                console.log(_this.$refs.keywords.value);
                this.$http.request({
                    url:_this.$url+'Search/',
                    method:"get",
                    params:val
                }).then(function (response) {
                    console.log(response);
                    _this.d3 = response.data
                }).catch(function (response) {
                    console.log(response)
                })
            }
        }
    }
</script>

<style scoped>
.content {
  color: aliceblue;
}
  @import "../assets/css/app.css"; /*引入外部css*/
  @import "../assets/css/custom.css";
</style>
