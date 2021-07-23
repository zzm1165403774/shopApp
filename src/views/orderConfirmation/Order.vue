<template>
    <div class="order">
        <div class="order__price">实付金额:<b>&yen;{{calculations.price}}</b></div>
        <div class="order__btn" @click="submit">提交订单</div>
    </div>
    <div class="mask" v-if="showMask">
        <div class="mask__content">
            <h3 class="mask__content__title">确认离开收银台？</h3>
            <p class="mask__content__desc">请尽快支付，否则将被取消</p>
            <div class="mask__content__btns">
                <div
                  @click="cancel"
                  class="mask__content__btn mask__content__btn--first"
                >取消订单</div>
                <div
                  @click="() => handleConfirm(false)"
                  class="mask__content__btn mask__content__btn--last"
                >确认支付</div>
            </div>
        </div>
    </div>
</template>
<script>
import { useCommonCart } from '../../effects/cartEffects'
import { useRouter, useRoute } from 'vue-router'
import { post } from '../../utils/request'
import { useStore } from 'vuex'
import { ref } from 'vue'
export default {
  name: 'Order',
  setup () {
    const router = useRouter()
    const route = useRoute()
    const store = useStore()
    const showMask = ref(false)

    const shopId = parseInt(route.params.id, 10)
    const { calculations, shopName, productList } = useCommonCart(shopId)
    const handleConfirm = async (isCanceled) => {
      const products = []
      // eslint-disable-next-line prefer-const
      for (let i in productList.value) {
        const product = productList.value[i]
        products.push({ id: product._id, num: product.count })
      }
      try {
        const result = await post('/api/order', {
          addressId: 1,
          shopId,
          shopName: shopName.value,
          isCanceled,
          products
        })
        console.log(result)
        if (result?.errno === 0) {
          store.commit('cleanCart', { shopId })
          router.push({ name: 'OrderList' })
        }
      } catch (e) {
        // changeToast('失败')
      }
    }
    const submit = () => {
      showMask.value = true
    }
    const cancel = () => {
      showMask.value = false
    }
    return { calculations, handleConfirm, showMask, submit, cancel }
  }
}
</script>
<style lang="scss" scoped>
.order{
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    display: flex;
    height: .49rem;
    line-height: .49rem;
    background-color: #fff;
    &__price{
        flex: 1;
        text-indent: .24rem;
        font-size: .14rem;
        color: #333;
    }
    &__btn{
        width: .98rem;
        background-color: #4FB09F;
        color: #fff;
        text-align: center;
        font-size: .14rem;
    }
}
.mask{
    position: absolute;
    z-index: 1;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    background-color: rgba(0,0,0,0.50);
    &__content{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 3rem;
        height: 1.5rem;
        background-color: #fff;
        border-radius: .04rem;
        text-align: center;
        &__title{
            margin: .24rem 0 0 0;
            font-size: .18rem;
            color: #333;
            line-height: .26rem;
        }
        &__desc{
            margin-top: .08rem 0 0 0;
            font-size: .14rem;
            color: #666;
        }
        &__btns{
            margin: .24rem .58rem;
            display: flex;
        }
        &__btn{
            flex: 1;
            width: .8rem;
            height: .32rem;
            line-height: .32rem;
            font-size: .14rem;
            border: .01rem solid #4fb0f9;
            border-radius: .16rem;
            &--first{
                margin-right: .24rem;
                color: #4fb0f9;
            }
            &--last{
                background-color: #4fb0f9;
                color: #fff;
            }
        }
    }
}
</style>
