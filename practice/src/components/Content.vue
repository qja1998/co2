<template>
    <div class="input-list">
        <input type="text" id="model_name" placeholder="Model" class="text-box"><br/>
        <input type="text" id="seq_len" placeholder="Seqeunce length" class="text-box"><br/>
        <input type="text" id="hidden" placeholder="Dimension of hidden layer" class="text-box"><br/>
        <input type="text" id="layer_num" placeholder="Number of layer" class="text-box"><br/>
        <input type="text" id="epochs" placeholder="Epochs" class="text-box"><br/>
        <input type="text" id="lr" placeholder="Learning rate" class="text-box"><br/>
        <button @click="train" class="btn">Train</button> <span>학습된 모델: {{ model_cnt }}</span>
        <span>
            <img v-if="is_trained" :src="result_img" class="result-img">
        </span>
    </div>
</template>

<!--html 속성 안의 데이터 바인딩 ->  :-->
<!--html 태그 안의 데이터 바인딩 -> {{  }}-->
<!--
    ui 현재 상태를 미리 data에 저장(모달창이 열렸는지 닫혔는지)
    데이터에 따라 ui가 어떻게 보일지 작성(그 상태에 따라 보이거나 숨기기 -> v-if)
-->
<script>
export default {
    name: 'App',
    data() {
        return {  // 자동 랜더링, soft coding (실시간으로 변해야 하는 값들을 바인딩)
            price : [100],
            model_cnt: 0,
            is_trained: false,
            result_img: require('@/assets/lstm-300-13938.png')
        }
    },
    methods: {
        train(){
            this.is_trained = true;
            this.model_cnt++;
        }
    },
    components: {
    }
};
</script>

<style>
.subject {
    color: blue;
    font-style: oblique;
    padding: 30px;
    text-align: center;
}
.userList {
    margin: 30px 0px 30px 0px;
}
.input-list {
    background: darkslateblue;
    padding: 15px;
    border-radius: 5px;
}
.text-box {
    color: white;
    padding: 10px;
}
.result-img {
    width: 90%;
    margin-top: 40px;
}
</style>