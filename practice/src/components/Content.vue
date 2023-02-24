<template>
    <div>
        <v-container fluid>
            <v-layout column>
                <v-flex xs12>
                    <h3 class="subject">User CRUD</h3>
                </v-flex>
                <v-flex column>
                    <v-form ref="form" v-model="valid" lazy-validation>
                        <input v-model="model_name" type="text" maxlength="4" placeholder="Model name"><br>
                        <input v-model="seq_len" type="number" placeholder="Sequence length"><br>
                        <input v-model="hidden" type="number" placeholder="Dimension of hidden layer"><br>
                        <input v-model="layer_num" type="number" placeholder="Number of layers"><br>
                        <input v-model="epochs" type="number" placeholder="Epochs"><br>
                        <input v-model="lr" type="number" placeholder="Learning rate"><br>

                        <button v-on:click="train" style="background: green">create</button>
                        <button v-on:click="clear" style="background: red">clear</button>
                    </v-form>
                </v-flex>

                <v-flex class="userList" column>
                    <v-card max-width="600" tile>
                        <v-list-item>
                            <v-list-item-content>
                                <v-list-item-title>Title</v-list-item-title>
                                <v-list-item-subtitle>content</v-list-item-subtitle>
                            </v-list-item-content>
                        </v-list-item>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
export default {};
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
</style>