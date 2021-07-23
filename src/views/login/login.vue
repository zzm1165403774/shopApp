<template>
    <div class="wrapper">
        <!-- <img class="wrapper__img" src="http://www.dell-lee.com/imgs/vue3/user.png"> -->
        <div class="wrapper__input">
            <input v-model="data.username" class="wrapper__input__content" placeholder="请输入手机号">
        </div>
        <div class="wrapper__input">
            <input v-model="data.password" type="password" class="wrapper__input__content" placeholder="请输入密码">
        </div>
        <div class="wrapper__login-button" @click="handleLogin">登陆</div>
        <div class="wrapper__login-link" @click="handleRegister">立即注册</div>
        <toast v-if="data.showToast" :message="data.toastMsg" />
    </div>
</template>

<script>
import { post } from '../../utils/request'
import { useRouter } from 'vue-router'
import { reactive } from 'vue'
import toast from '../../components/toast'

export default {
  name: 'login',
  components: { toast },
  setup () {
    const router = useRouter()
    const changeToast = (message) => {
      data.showToast = true
      data.toastMsg = '登陆失败'
      setTimeout(() => {
        data.showToast = false
        data.toastMsg = ''
      }, 1000)
    }
    const data = reactive({
      username: '',
      password: '',
      showToast: false,
      toastMsg: ''
    })
    const handleLogin = async () => {
      try {
        const result = await post('/api/user/login', {
          username: data.username,
          password: data.password
        })
        if (result?.errno === 0) {
          localStorage.isLogin = true
          router.push({ name: 'Home' })
        } else {
          changeToast('登陆失败')
        }
      } catch (e) {
        changeToast('失败')
      }
    }
    const handleRegister = () => {
      router.push({ name: 'Register' })
    }
    return { data, handleLogin, handleRegister }
  }
}
</script>

<style lang="scss" scoped>
.wrapper{
    position: absolute;
    top: 50%;
    left: 0;
    right: 0;
    transform: translateY(-50%);
    &__img{
        width: .66rem;
        height: .66rem;
        display: block;
        margin: 0 auto .4rem auto;
    }
    &__input{
        background: #F9F9F9;
        height: .48rem;
        margin: 0 .4rem .16rem .4rem;
        padding: 0 .16rem;
        border: 1px solid rgba(0,0,0,0.10);
        border-radius: 6px;
        &__content{
            line-height: .48rem;
            border: none;
            outline: none;
            width: 100%;
            background: none;
            font-size: .16rem;
            color: rgba(0,0,0,0.80);
            &::placeholder{
                color: #777
            }
        }
    }
    &__login-button{
        margin: .32rem .4rem .16rem .4rem;
        line-height: .48rem;
        background: #0091FF;
        box-shadow: 0 .04rem .08rem 0 rgba(0,145,255,0.32);
        border-radius: .04rem;
        color: white;
        font-size: .16rem;
        text-align: center;
    }
    &__login-link{
        font-size: .14rem;
        color: #777;
        text-align: center;
    }
}
</style>
