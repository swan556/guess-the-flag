<script lang="ts">
    
    let country_name: string = $state("");
    let country_code: string = $state("");
    let score: number = $state(0);
    let error: string = $state("");

    let dataset: string = "/flags_dataset/Flags/";
    let answer = $state("");
    
    

    const getRandomFlag = async () => {

        error = "";
        if(answer === country_name) {
            score++;
        }
        else score--;

        answer = "";

        const fetch_flag = async() => {
            const res = await fetch('http://127.0.0.1:5000/random-flag');
            let country = await res.json();

            country_name = country.country_name;
            country_code = country.country_code;
        }

        fetch_flag();
        if(answer === "") {
            error = "no empty spaces alowed";
        }


        }

</script>

<div class="app">
    <div class="container">
        <div class="heading">
            Guess The Flag!
        </div>

        <div class="flag">
            <img src={dataset + country_code + ".png"} alt="flag" />

        </div>

        <div class="options">
            <label for="input">Answer</label>
            <input type="text" bind:value={answer} id="input" />
        </div>

        <div class="next">
            <button class="nextButton" onclick={getRandomFlag}>Next</button>
        </div>
        <div>score: {score}</div>
        <div>your ans: {answer}</div>
        <div>country name: {country_name}</div>

        {#if (error !== "")}
            <div style="color: red;">{error}</div>
        {/if}
    </div>
</div>


<style>
    .app {
        display: flex;
        align-items: center;
        align-self: center;
        justify-content: center;
    }

    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>