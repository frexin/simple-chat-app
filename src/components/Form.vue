<template>
    <div class="msg-form">
        <form @submit.prevent="formSubmit">
            <div class="form-author-name">
                <input v-model="author" type="text" :disabled="savedAuthor" name="author_name" placeholder="Enter your name"/>
            </div>
            <div class="form-elements">
                <div class="form-msg-area"><textarea v-model="text" name="message_text"></textarea></div>
                <div class="form-submit"><input type="submit" name="submit" value="Send"/></div>
            </div>
        </form>
    </div>
</template>

<script>
    export default {
        name: "Form",
        data: () => {
            return {
                author: null, text: null, savedAuthor: null
            }
        },
        mounted() {
            this.author = window.localStorage.getItem('authorName');
            this.savedAuthor = this.author;
        },
        methods: {
            formSubmit: function() {
                this.saveAuthorName();

                let msg = {
                    date: new Date().toLocaleString(),
                    author: this.author,
                    text: this.text
                };

                this.$emit('formSubmit', msg);

                this.text = null;
            },

            saveAuthorName: function () {
                if (this.author) {
                    window.localStorage.setItem('authorName', this.author);
                    this.savedAuthor = this.author;
                }
            }
        }
    }
</script>

<style scoped>
    .msg-form {
        padding: 15px;
        background-color: #EEEDED;
    }

    .form-elements {
        display: flex;
        align-items: center;
    }

    .form-msg-area {
        flex-grow: 1;
    }

    .form-msg-area textarea {
        background-color: #FEFEFE;
        border: none;
        min-height: 85px;
        width: 100%;
        font-family: inherit;
    }

    .form-submit input {
        width: 75px;
        height: 50px;
        background-color: #128C7E;
        border: none;
        border-radius: 10px;
        margin-left: 15px;
        color: #fff;
        font-weight: bold;
        font-size: 16px;
    }

    .form-submit input:hover {
        background-color: #075E54;
    }

    .form-author-name input {
        width: 100%;
        margin-bottom: 10px;
        border: none;
        height: 30px;
        text-indent: 10px;
    }
</style>
