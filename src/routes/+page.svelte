<script lang="ts">
	let country_name: string = $state('');
	let country_code: string = $state('');
	let score: number = $state(0);
	let error: number = $state(0);
	let startScreen: boolean = $state(true);

	let dataset: string = '/flags_dataset/Flags/';
	let answer = $state('');

	const fetch_flag = async () => {
		fetch("https://flag-guess-game-be.up.railway.app/")
            .then(res => res.json())
            .then(data => {
                country_name = data.country_name;
		        country_code = data.country_code;
            });

            console.log("fetched: ", country_name, "  ", country_code);
	};

	const toDashedString = ({ str }: { str: string }): string => {
		let modified_str: string = '';
		for (let i = 0; i < str.length; i++) {
			if (str[i] === ' ') modified_str += '\x20';
			else modified_str += '[]';
		}

		return modified_str;
	};

	const checkAns = ({ startMenu }: { startMenu: boolean }) => {
		if (!startMenu) {
			if (answer !== '') {
				if (answer.trim().toLowerCase() === country_name.toLowerCase()) {
					score += 1;
				} else score -= 1;

				error = 0;
				answer = '';
				fetch_flag();
			} else {
				error = 1;
			}
		} else {
			startScreen = false;
			fetch_flag();
		}
	};
</script>

<div class="app">
    <img src="bg.jpeg" alt="bg" class="bg-img"/>
	{#if startScreen}
		<div class="container">
			<div class="start">
				<button
					class="startButton"
					onclick={() => {
						checkAns({ startMenu: true });
					}}>START GAME</button
				>
			</div>
		</div>
	{:else}
		<div class="container">
            
			<div class="heading">Guess The Flag!</div>
            <div style="margin-top: 100px; background-color:azure; color:black; border-radius: 6px; width:120px; height:60px; font-size:25px; justify-elements:center">score: {score}</div>
			<div>
				<img
					src={dataset + country_code + '.png'}
					alt="flag"
					style="background-size: cover;"
                    class="flag"
				/>
			</div>

			<div class="answer">
				<input
					type="text"
                    class="input"
					bind:value={answer}
					id="input"
                    placeholder="answer"
					onkeydown={(e) => {
						if (e.key === 'Enter') {
							checkAns({ startMenu: false });
						}
					}}
				/>
			</div>

			<div class="next">
				<button
					class="nextButton"
					onclick={() => {
						checkAns({ startMenu: false });
					}}>Next</button
				>
			</div>
			
			<div class="hint">Hint: {toDashedString({ str: country_name })}</div>

			{#if error}
				<div style="color: red;">You cannot submit blank answer</div>
			{/if}
		</div>
        <div>this is the answer:::  {country_code} : {country_name}</div>
	{/if}
</div>

<style>
    body {
        box-sizing: border-box;
        padding: 0;
        margin: 0;
    }
	.app {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh; /* fills the viewport */
        background-color: #313131;
        
    }

    .bg-img {
        position: absolute;
        top: 0%;
        left: 0%;
        width: 100dvw;
        height: 100dvh;
        /* z-index: -1; */
        opacity: 0.5;
    }

    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center; /* vertical + horizontal centering */
        flex: 1; /* fills parent .app */
        height: 100dvh;
        width: 100dvw; /* optional if you want full width */
        /* background-image: url("/bg.jpeg");
        opacity: 0.5;
        background-size: cover;
        background-repeat: repeat-y;
        background-position: center; */
        z-index: 10;
    }


    .startButton {
        position: absolute;
        top:50%;
        bottom: 50%;

        transform: translate(-50%, -50%);

        border-radius: 8px;
        width: 500px;
        height: 200px;
        outline: none;
        border: 7px solid;
        border-color: rgb(201, 187, 0);
        border-radius: 50px;
        background-color: black;
        color: white;
        font-size: 40px;
        font-style:normal;
        font-family:Georgia, 'Times New Roman', Times, serif;

        transition: border-color 0.5s ease, box-shadow 0.5s ease;
    }

    .startButton:hover {
        border-color: transparent;
        box-shadow: 0 0 20px 5px limegreen;
        font-size: 50px;
        color: rgb(0, 250, 104);
    }

    .heading {
        font-family: "Comic Sans MS", "Comic Sans", cursive;
        color: white;
        font-size: 100px;
        margin-top: 30px;
        font-weight: 1000;

        background-color: rgba(0,0,0, 0.5);
        border-radius: 20px;
    }

    .flag {
        border: 10px solid;
        border-color: white;
        border-radius: 10px;
        margin-top: 10px;
    }

    .answer {
        margin-top: 30px;
        color: white;
    }

    .next {
        margin-top: 30px;
    }

    .nextButton {
        width: 200px;
        height: 50px;
        outline: none;
        border: 3px solid;
        border-radius: 20px;
        border-color: violet;
        background-color: rgb(255, 255, 255);
    }

    .hint {
        color: black;
        font-size: 40px;
        background-color: rgba(255, 255, 255, 1);
        border-radius: 10px;
        margin-top: 30px;
    }

    .input {
        text-align: center;
        border-radius: 6px;
        width: 400px;
        height: 30px;
        font-size: 26px;
    }
    .input::placeholder {
        text-align: center;
    }

</style>
