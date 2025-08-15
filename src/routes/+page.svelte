<script lang="ts">
    
    let country_name: string = $state("");
    let country_code: string = $state("");
    let score: number = $state(0);
    let error: number = $state(0);
    let startScreen: boolean = $state(true);

    let dataset: string = "/flags_dataset/Flags/";
    let answer = $state("");
    
    
    const fetch_flag = async() => {
        const res = await fetch('http://127.0.0.1:5000/random-flag');
        let country = await res.json();

        country_name = country.country_name;
        country_code = country.country_code;
    }

    const toDashedString = ({str} : {str: string}): string => {
        let modified_str: string = "";
        for(let i = 0; i < str.length; i++) {
            if(str[i] === " ") modified_str += "\x20";
            else modified_str += "[]"
        }

        return modified_str;
    }


    const checkAns = ({startMenu}: {startMenu: boolean}) => {
        
        if(!startMenu)
        { 
            if(answer !== "") {
                if(answer.trim().toLowerCase() === country_name.toLowerCase()) {
                    score += 1;
                }
                else score -= 1;

                error = 0;
                answer = "";
                fetch_flag();
            }

            else {
                error =1;
            }}
        else {
            startScreen = false;
            fetch_flag();
        }
    }

</script>

<div class="app">

    {#if (startScreen)}
        <div class="container">
            <div class="start">
                <button class="startButton" onclick={() => {
                    checkAns({startMenu: true});
                }}>START GAME</button>
            </div>
        </div>
    {:else}
        <div class="container">
            <div class="heading">
                Guess The Flag!
            </div>

            <div class="flag">
                <img src={dataset + country_code + ".png"} alt="flag" style="width: 300px; height: 200px;" />
            </div>

            <div class="options">
                <label for="input">Answer</label>
                <input type="text" bind:value={answer} id="input" onkeydown={(e) => {
                    if(e.key === "Enter") {
                        checkAns({startMenu: false});
                    }
                }}/>
            </div>

            <div class="next">
                <button class="nextButton" onclick={() => {checkAns({startMenu: false})}}>Next</button>
            </div>
            <div>score: {score}</div>
            <div>your ans: {answer}</div>
            <div>Hint: {toDashedString({str: country_name})}</div>

            {#if (error)}
                <div style="color: red;">You cannot submit blank answer</div>
            {/if}
        </div>

    {/if}
</div>


<style>
    .app {
        display: flex;
        align-items: center;
        align-self: center;
        justify-content: center;
        height: 100vh;
    }

    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }


</style>