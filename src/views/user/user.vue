<template>
    <div class="wrapper">
      <div class="usertop">
        <div class="usertop__info" v-if="isLogin">
          <div @click="handleLogout" class="usertop__logout iconfont">&#xe65c;</div>
          <div class="usertop__info__name">ziming</div>
          <div class="usertop__info__id">1321315465465</div>
          <div class="usertop__info__icons">
            <router-link to="/"><span class="usertop__info__icon iconfont">&#xf4dc;</span></router-link>
            <router-link to="/orderList"><span class="usertop__info__icon iconfont">&#xf4db;</span></router-link>
            <router-link to="/cartList"><span class="usertop__info__icon iconfont">&#xf4e9;</span></router-link>
            <span class="usertop__info__icon iconfont">&#xf4df;</span>
          </div>
        </div>
        <div class="usertop__info" v-if="!isLogin">
          <div class="usertop__info__name">未登录，请先登陆</div>
          <router-link to="/Login"><div class="button">登陆</div></router-link>
        </div>
        <img class="img" src="http://www.dell-lee.com/imgs/avatar.jpg">
      </div>
    </div>
    <Docker :currentIndex ="3" />
</template>
<script>
import Docker from '../../components/docker'
import { useRouter } from 'vue-router'
export default {
  name: 'User',
  components: { Docker },
  setup () {
    const router = useRouter()
    const handleLogout = () => {
      localStorage.removeItem('isLogin')
      router.push({ name: 'Home' })
    }
    const { isLogin } = localStorage
    return { isLogin, handleLogout }
  }
}
</script>
<style lang="scss" scoped>
a{
  text-decoration: none;
}
.wrapper{
  overflow-y: auto;
  position: absolute;
  left: 0;
  top: 0;
  bottom: .5rem;
  right: 0;
  background-image: linear-gradient(239deg, #3A6FF3 0%, #50C7FB 100%);
}
.usertop{
  position: relative;
  height: 1.5rem;
  padding-top: .4rem;
  &__logout{
    position: absolute;
    right: .4rem;
    font-size: .3rem;
  }
  &__info{
    margin: 1.6rem .18rem 0 .18rem;
    height: 2rem;
    padding-top: .46rem;
    background: rgba($color: #fff, $alpha: 0.8);
    border-radius: .08rem;
    box-shadow: .03rem .03rem slategrey;
    &__name {
      margin-top: .14rem;
      font-size: .24rem;
      color: #262628;
      text-align: center;
      line-height: .36rem;
    }
    &__id {
      margin-top: .14rem;
      font-size: .14rem;
      color: #C1C0C9;
      text-align: center;
    }
    &__icons{
      margin: .5rem 0;
      line-height: .4rem;
      text-align: center;
    }
    &__icon{
      padding: .04rem;
      margin: .1rem;
      color: #333;
      font-size: .3rem;
      border-radius: 50%;
      border: .01rem solid #fff;
      box-shadow: .01rem .01rem slategrey;
    }
  }
}
.button{
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  background-color: #3A6FF3;
  margin-top: .5rem;
  height: .3rem;
  width: .8rem;
  line-height: .3rem;
  font-size: .14rem;
  border-radius: .06rem;
  text-align: center;
  color: #fff;
}
.img{
  position: absolute;
  top: 1.4rem;
  left: 50%;
  transform: translateX(-50%);
  width: 1rem;
  height: 1rem;
  border-radius: 50%;
}
</style>
