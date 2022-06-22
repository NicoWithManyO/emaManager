
import discord
from discord.ext import commands


class Confirm(discord.ui.View):
    def __init__(self, instantiator):
        super().__init__()
        self.instantiator = instantiator
        self.value = None

    @discord.ui.button(label="Confirmer & valider", style=discord.ButtonStyle.green)
    async def confirm(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user == self.instantiator:
            self.value = True
            self.stop()
        else:
            await interaction.response.send_message(f"> 🚫 Désolé, {interaction.user.display_name}, seul {self.instantiator.display_name} peut faire cela !", ephemeral=False)

    @discord.ui.button(label="Annuler", style=discord.ButtonStyle.red)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user == self.instantiator:
            self.value = False
            self.stop()
        else:
            await interaction.response.send_message(f"> 🚫 Désolé, {interaction.user.display_name}, seul {self.instantiator.display_name} peut faire cela !", ephemeral=False)

